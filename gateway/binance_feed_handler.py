import websocket;
import json;
import socket;
import struct;
import time;
import threading;

# CONFIGURATION
SYMBOL = "btcusdt"
WS_URL = f"wss://stream.binance.com:9443/ws/{SYMBOL}@trade"

UDP_IP = "127.0.0.1"
UDP_PORT = 1234

STRUCT_FORMAT = "8sddQQ" # follows C++ struct below
# struct Trade {
#     char symbol[8];
#     double price;
#     double quantity;
#     uint64_t timestamp;
#     uint64_t trade_id;
# };

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def on_message(ws, message):
    try:
        data = json.loads(message)
        symbol_str=data['s']
        price = float(data['p'])
        quantity = float(data['q'])
        timestamp = int(data['T'])
        trade_id = int(data['t'])
        
        symbol_bytes = symbol_str.encode('utf-8')
        if len(symbol_str) > 8:
            symbol_bytes = symbol_bytes[:8]
        else:
            symbol_bytes = symbol_bytes.ljust(8, b'\x00')
            
        binary_packet = struct.pack(f"<{STRUCT_FORMAT}", symbol_bytes, price, quantity, timestamp, trade_id) 
        
        sock.sendto(binary_packet, (UDP_IP, UDP_PORT))
        print(f"Sent: {symbol_str} Price: {price} Qty: {quantity} Time: {timestamp} TradeID: {trade_id}")
    except Exception as ex:
        print(f"Failed to Process: {ex}")
    pass

def on_error(ws, error):
    print(f"Error: {error}")
    pass

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")
    pass

def on_open(ws):
    print(f"Connected to {WS_URL}, forwarding trades to UDP {UDP_IP}:{UDP_PORT}")
    pass

if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(WS_URL, on_close=on_close, on_message=on_message, on_error=on_error, on_open=on_open)
    ws.run_forever()