FROM python:3.11
LABEL Maintainer="nithin98"
WORKDIR /Users/nithinsaikrishna/Documents/yt_docker/
COPY yt_analytics.py ./
COPY yt_requirements.txt ./
COPY client_secret_desktop_temp1.json ./
RUN python -m pip install --upgrade pip
RUN pip install -r yt_requirements.txt
CMD ["python", "./yt_auth.py"]
COPY "run.sh" .
RUN ["chmod", "+x", "./run.sh"]
ENTRYPOINT [ "./run.sh" ]
#CMD ["open", "./yt_analytics.csv"]
