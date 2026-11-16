# Frame server for the 3D studio: serves the scene page to headless Chrome, receives each rendered frame over HTTP,
# and pipes the frames (plus the audio mix) into ffmpeg.  Usage: python render.py PAGE.html OUT.mp4 [AUDIO.wav] [--stills]
import http.server, os, subprocess, sys, threading, time, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
FFMPEG = '/opt/anaconda3/bin/ffmpeg'
page, out = sys.argv[1], sys.argv[2]
audio = sys.argv[3] if len(sys.argv) > 3 and not sys.argv[3].startswith('--') else None
query = next((a[4:] for a in sys.argv if a.startswith('--q=')), '')
state = {'n': 0, 'done': False, 'ff': None, 'log': []}

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=HERE, **k)
    def log_message(self, *a): pass
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store'); super().end_headers()
    def do_POST(self):
        body = self.rfile.read(int(self.headers.get('Content-Length', 0)))
        if self.path.startswith('/frame'):
            if state['ff'] is None:
                cmd = [FFMPEG, '-y', '-v', 'error', '-f', 'image2pipe', '-c:v', 'mjpeg', '-r', '25', '-i', '-']
                if audio: cmd += ['-i', audio]
                cmd += ['-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p']
                if audio: cmd += ['-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-c:a', 'aac', '-b:a', '160k', '-shortest']
                state['ff'] = subprocess.Popen(cmd + ['-movflags', '+faststart', out], stdin=subprocess.PIPE)
            state['ff'].stdin.write(body); state['n'] += 1
        elif self.path.startswith('/log'): state['log'].append(body.decode('utf-8', 'ignore')); print('page:', state['log'][-1], flush=True)
        elif self.path.startswith('/done'): state['done'] = True
        self.send_response(200); self.send_header('Content-Length', '0'); self.end_headers()

srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), H); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
prof = tempfile.mkdtemp(prefix='studio3d')
ch = subprocess.Popen([CHROME, '--headless=new', '--hide-scrollbars', '--force-device-scale-factor=1', '--window-size=1080,1920',
                       '--use-angle=metal', '--enable-gpu', '--ignore-gpu-blocklist', '--enable-unsafe-swiftshader', '--user-data-dir=' + prof,
                       '--remote-debugging-port=0', 'http://127.0.0.1:%d/%s?%s' % (port, page, query)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
t0 = time.time(); last = (0, t0)
while not state['done']:
    time.sleep(1)
    if state['n'] != last[0]: last = (state['n'], time.time())
    if time.time() - last[1] > 90: print('STALLED at frame', state['n']); break
ch.terminate()
if state['ff']: state['ff'].stdin.close(); state['ff'].wait()
print('frames', state['n'], 'in %.0fs' % (time.time() - t0), '->', out)
