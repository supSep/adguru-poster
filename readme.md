1) run redis-server

2) run python3.4 /usr/local/bin/rqworker
    |-> additionally run rqinfo

3) test via http://localhost:5000/vancouver/post/
    |-> follow json
    {
    "id": "2",
  	"title" : "sep",
    "category": "lol",
    "location": "lol",
    "email": "muck@muck.com",
    "phone": "123-123-1234",
    "description":"this shit right here my nigga",
    "price": 123
}