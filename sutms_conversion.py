
#!/bin/sh 
i=0
while [ $i -le 1 ];  
do  
  curl -kv -o 'ioc_updates' -H 'Content-Type: application/json' 'threat feed webui' -d '{"token":"token_number", "query":"confidence>5
0 AND severity=very-high AND date_last>-1d", "type":"csv", "size":100}'  
  perl -lne '/\b[0-9.]{7,15}\b/ && print $&'  ioc_updates >blacklisted_IP
"$i";
i=$(($i+1));
done
