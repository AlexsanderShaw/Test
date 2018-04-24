# def lazy_sum(*args):
# 		def sum():
# 			ax = 0
# 			for n in args:
# 				ax = ax + n
# 			return ax
# 		return sum		

# f = lazy_sum(1,3,5,7)	
# f

# f()	
# 
# 
# 





#设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import functools, time

def metric(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		start = time.time()
		v = func(*args,**kw)
		print('%s executed in %s ms' % (func.__name__, time.time()-start))
		return func
	return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

print(fast.__name__)
print(slow.__name__)    


# def log(text):
# 	def decorator(func):
# 		def wrapper(*args,**kw):
# 			print('%s %s():' % (text,func.__name__))
# 			return func(*args, **kw)
# 		return wrapper
# 	return decorator


# @log('execute')	
# def now():
# 	print('2123124')			

# now()	
# print(now.__name__)		