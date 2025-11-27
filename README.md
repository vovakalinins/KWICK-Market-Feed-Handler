# KWICK (Linux)
## Supported Markets: 
- BTC on Binance ($BTCUSDT)
## What Is It?
This is supposed to emulate market feed handling of a real exchange, modeled after ones that are used in HFTs (High Frequency Trading) while ensuring the lowest && deterministic possible amount of latency. It will only run on linux due to kernel bypassing.
## How Will You Ensure Low and Predictible Latency.
- Custom Slab Allocation: https://en.wikipedia.org/wiki/Slab_allocation
- Kernel Bypass (io_uring): https://man7.org/linux/man-pages/man7/io_uring.7.html
- Lock-Free SPSC
## How Will You Make It Close to Real HFT Handlers?
- Since I don't have access to any real data feeds like NASDAQ (which sends in UDP), I am using Binance's websocket for BTCUSDT, converted to a UDP Binary for realism using a python gateway. (But doesnt this increase latency? Yes, but I am not measuring network latency, I am measuring the latency between data in and data process.)
- I also might add kdb+ to do some logging.
## Installing & Instructions
Coming Soon.