import threading
import time

# 创建变量
g_num = 0
# 创建锁默认为开锁状态
mutex = threading.Lock()


def test1(num):
    global g_num
    for i in range(num):
        # 上锁
        mutex.acquire()
        g_num += 1
        # 解锁
        mutex.release()
        print("test1"+str(g_num) )
    print("--- test1 线程 g_num = %d---" % g_num)


def test2(num):
    global g_num
    for i in range(num):
        # 上锁
        mutex.acquire()
        g_num += 1
        # 解锁
        mutex.release()
        print("test2"+ str(g_num) )
    print("--- test2 线程 g_num = %d---" % g_num)


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    # time.sleep(1)
    t2.start()

    time.sleep(1)
    print("--- 主线程 g_num = %d---" % g_num)


if __name__ == '__main__':
    main()