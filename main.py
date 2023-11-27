import os

import uvicorn


if __name__ == '__main__':
    uvicorn.run('simpsons:app', host='0.0.0.0', port=8190, reload=True)
