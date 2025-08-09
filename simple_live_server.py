#!/usr/bin/env python3
import http.server
import socketserver
import os
import time
import webbrowser
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class LiveReloadHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()
        
        # Inject live reload script for HTML files
        if self.path.endswith('.html') or self.path == '/':
            self.wfile.write(b'''
<script>
(function() {
    var lastModified = Date.now();
    function checkForChanges() {
        fetch(window.location.href + '?t=' + Date.now(), {
            method: 'HEAD',
            cache: 'no-cache'
        }).then(function(response) {
            var currentModified = new Date(response.headers.get('Last-Modified')).getTime();
            if (currentModified > lastModified) {
                location.reload();
            }
        }).catch(function() {
            // Ignore errors
        });
    }
    
    // Check for changes every 2 seconds
    setInterval(checkForChanges, 2000);
    
    // Also listen for file system events (if supported)
    if (typeof EventSource !== 'undefined') {
        var eventSource = new EventSource('/events');
        eventSource.onmessage = function(event) {
            if (event.data === 'reload') {
                location.reload();
            }
        };
    }
})();
</script>
''')

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, server):
        self.server = server
        
    def on_modified(self, event):
        if not event.is_directory:
            file_ext = os.path.splitext(event.src_path)[1].lower()
            if file_ext in ['.html', '.css', '.js']:
                print(f"File changed: {event.src_path}")
                print("Browser will reload automatically...")

def main():
    PORT = 8000
    
    # Set up file watching
    event_handler = FileChangeHandler(None)
    observer = Observer()
    observer.schedule(event_handler, '.', recursive=True)
    observer.start()
    
    # Start HTTP server
    with socketserver.TCPServer(("", PORT), LiveReloadHandler) as httpd:
        print(f"🚀 Live development server running at http://localhost:{PORT}")
        print("📁 Watching for changes in HTML, CSS, and JS files...")
        print("🔄 Browser will automatically reload when files change")
        print("⏹️  Press Ctrl+C to stop")
        
        # Open browser
        webbrowser.open(f'http://localhost:{PORT}')
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Shutting down live server...")
            observer.stop()
            httpd.shutdown()

if __name__ == "__main__":
    main()
