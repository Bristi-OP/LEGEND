FROM python:3.9
WORKDIR /userbot
RUN git clone https://github.com/Bristi-OP/MEGASTAR.git .
RUN pip3 install -U -r requirements.txt
ENV PATH="/home/userbot/bin:$PATH"
CMD ["bash", "start.sh"]
