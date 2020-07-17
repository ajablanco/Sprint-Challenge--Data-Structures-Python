class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # define oldest elements index
        self.oldest_el_index = 0
        # initialize ring_buffer
        self.ring_buffer = []

    def append(self, item):
        # check if length of ring_buffer is less than capacity
        if len(self.ring_buffer) < self.capacity:
            # append item
            self.ring_buffer.append(item)
        # else
        else:
            # reassign oldest el to new item
            self.ring_buffer[self.oldest_el_index] = item
            # increment oldest el index
            self.oldest_el_index += 1
        # if oldest el is at capacity, reset it to 0
        if self.oldest_el_index == self.capacity:
            self.oldest_el_index = 0
    def get(self):
        return self.ring_buffer