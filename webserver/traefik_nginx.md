## traefik vs nginx 
## put spa
### nginx  
- nginx has ability to serve static files directly from disk 
- so you can bundled SPA mount 
### traefik 
- traefik is not statics server 
- the `spa-to-http` work out of the box without configuration

### dash board
https://devforth.io/blog/nginx-vs-traefik-how-slower-one-can-be-better/


### performance 
- traefik is slower 15% than nginx 
- but the traefik3.0 will be faster 20% than last version

## practice 
- https://dev.to/tiangolo/deploying-fastapi-and-other-apps-with-https-powered-by-traefik-5dik