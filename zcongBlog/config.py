TORNADO_SETTINGS={
    "debug":True,
    "static_path":'/static',
    "gzip":True,
    "xsrf_cookies":True,
    #"cookie_secret":"",
    "template_path":"templates",    
}
GLOBAL_SETTINGS={
    "Default_Port":8088,
    "Mode":"develop", #develop test deploy
    "Log_Prefix":"log/",
    "DB":{
        'Develop':{
            'Host':'127.0.0.1:3307',
            'Name':'zcong',
            'User':'zcong',
            'Psw':'zcong',
        },
        'Test':{
            'Host':'',
            'Name':'',
            'User':'',
            'Psw':'',
        },
        'Deploy':{
            'Host':'',
            'Name':'',
            'User':'',
            'Psw':'',
        },
    }
}