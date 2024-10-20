import math
import time
def consume_cpu():
    x = 1
    start_time = time.time()
    while True:
        x = x +1
        if time.time() - start_time > 3000:
            print("Đã chạy quá 3000 giây, tự động kết thúc.")
            break
        if x > 1000:
            x = 1
        time.sleep(0.1)

consume_cpu()