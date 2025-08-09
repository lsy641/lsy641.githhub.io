#!/usr/bin/env python3
import http.server
import socketserver
import os
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import webbrowser

class LiveReloadHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers and live reload script
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
        
        # Inject live reload script for HTML files
        if self.path.endswith('.html') or self.path == '/':
            self.wfile.write(b'''
<script>
(function() {
    var ws = new WebSocket('ws://localhost:8080');
    ws.onmessage = function() {
        location.reload();
    };
    ws.onclose = function() {
        console.log('Live reload disconnected');
    };
})();
</script>
''')

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, websocket_server):
        self.websocket_server = websocket_server
        
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File changed: {event.src_path}")
            # Notify connected clients to reload
            self.websocket_server.notify_clients()

class SimpleWebSocketServer:
    def __init__(self):
        self.clients = []
        
    def notify_clients(self):
        # Simple implementation - in a real scenario you'd use a proper WebSocket library
        print("Notifying clients to reload...")

def main():
    PORT = 8000
    WS_PORT = 8080
    
    # Create WebSocket server for live reload
    ws_server = SimpleWebSocketServer()
    
    # Set up file watching
    event_handler = FileChangeHandler(ws_server)
    observer = Observer()
    observer.schedule(event_handler, '.', recursive=True)
    observer.start()
    
    # Start HTTP server
    with socketserver.TCPServer(("", PORT), LiveReloadHandler) as httpd:
        print(f"Live server running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop")
        
        # Open browser
        webbrowser.open(f'http://localhost:{PORT}')
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down...")
            observer.stop()
            httpd.shutdown()

if __name__ == "__main__":
    main()
