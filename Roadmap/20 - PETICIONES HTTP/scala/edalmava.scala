// Usando la librería sttp

import sttp.client3.quick.*
import sttp.client3.HttpClientSyncBackend
import sttp.client3.Response

val backend = HttpClientSyncBackend()

val request = quickRequest
  .get(uri"https://httpbin.org/get")

val response = request.send(backend)

if response.is200 then
  println(response.body)
else 
  println(s"El servidor ha devuelto el código: ${response.code}")
