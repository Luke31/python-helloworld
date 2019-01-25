FROM frolvlad/alpine-miniconda3 as builder
COPY environment.yml /app/
RUN conda env create --file app/environment.yml -p /env
COPY . /app

WORKDIR /app
RUN source activate /env && pip install . && pytest --flakes

FROM frolvlad/alpine-miniconda3

MAINTAINER Lukas Schmid

EXPOSE 5000
COPY --from=builder /env /env
COPY --from=builder /app/run.py /app/run.py
WORKDIR /app
CMD source activate /env && python run.py
