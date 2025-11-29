#pragma once

#include <cstdint>
#include <iostream>

struct TradeMessage {
  char symbol[8];
  double price;
  double quantity;
  uint64_t timestamp;
  uint64_t trade_id;
};

constexpr int UDP_PORT = 1234;
constexpr const char* UDP_IP = "127.0.0.1";
constexpr size_t RING_BUFFER_SIZE = 1024 * 16;
