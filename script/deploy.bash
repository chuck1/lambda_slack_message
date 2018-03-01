
here=`pwd`

zip deployment.zip lambda_function.py
#zip -r deployment.zip <package folder>

cd env/lib/python3.6/site-packages/

zip -r $here/deployment.zip slackclient
zip -r $here/deployment.zip requests
zip -r $here/deployment.zip urllib3
zip -r $here/deployment.zip chardet
zip -r $here/deployment.zip certifi
zip -r $here/deployment.zip idna
zip -r $here/deployment.zip websocket

cd $here

python script/deploy.py $here/deployment.zip


