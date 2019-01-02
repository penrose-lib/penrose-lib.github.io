---
category: Get
path: '/get'
title: 'Packages'
type: 'GET'

layout: none
---

While it's recommended to use one of the clients to parse the output
for you, you are free to interact with the endpoints without them.

### API Base

The API base provides a summary of links to all endpoints. 

```
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET https://penrose-lib.github.io/api.json
```

### Library

The library includes a listing of all packages, including dsl, sty, and sub.

```bash

curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET https://penrose-lib.github.io/library.json

```

### Packages

Alternately, you can filter to just a specific package type.

**dsl**

```bash

curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET https://penrose-lib.github.io/dsl.json

```

**sub**

```bash
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET https://penrose-lib.github.io/sub.json
```

**sty**

```bash
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET https://penrose-lib.github.io/sty.json
```

We will add additional endpoints (and filters) as needed.
