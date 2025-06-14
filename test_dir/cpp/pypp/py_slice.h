#pragma once

#include <optional>
#include <vector>

struct PySlice {
    int start;
    std::optional<int> stop;
    int step;

    PySlice(int start, std::optional<int> stop, int step = 1)
        : start(start), stop(stop), step(step) {}
};

std::vector<int> compute_slice_indices(int start, std::optional<int> stop,
                                       int step, int n);
