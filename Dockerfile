# Imagem base leve do Nginx
FROM nginx:1.27-alpine

# Copia a página estática para a pasta que o Nginx serve
# Se seu index.html está na raiz do repo, este COPY funciona direto.
COPY index.html /usr/share/nginx/html/index.html

# Expõe a porta HTTP padrão do Nginx
EXPOSE 80

# Comando padrão do Nginx em 1 processo
CMD ["nginx", "-g", "daemon off;"]
