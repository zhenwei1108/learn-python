class default_params:
    def say_ok(message, time = 1, switch=True):
        if switch:
            print(time*message)
        else:
            print("nothing")

#默认参数
if __name__ == '__main__':
    default_params.say_ok("this is test ")
    default_params.say_ok("this is test ", 2)
    default_params.say_ok("this is test ", 3,False)