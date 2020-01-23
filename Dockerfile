FROM lambci/lambda:python3.8

ENV AWS_DEFAULT_REGION us-west-2
ENV APP_DIR /var/task

ADD . .

CMD pip install -r requirements.txt -t $APP_DIR
#  zip -9 deploy_package.zip pepup.py && \
#  zip -r9 deploy_package.zip *

RUN python pepup_login.py '{"Hello":"World"}'
RUN ls -l
#RUN cat hello.txt
