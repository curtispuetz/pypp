#pragma once

#include <optional>

int calc_stop_index(std::optional<int> stop, int step, int collection_size);
int calc_start_index(std::optional<int> start, int step, int collection_size);
