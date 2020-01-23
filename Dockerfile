FROM lambci/lambda:python3.7

ENV AWS_DEFAULT_REGION us-west-2
ENV APP_DIR /var/task

ADD . .

CMD pip install -r requirements.txt -t $APP_DIR && \
  zip -9 deploy_package.zip pepup_devel.py && \
  zip -r9 deploy_package.zip *

#RUN python pepup_login.py '{"Hello":"World"}'
RUN ls -l
#RUN cat hello.txt
