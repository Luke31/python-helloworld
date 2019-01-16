FROM frolvlad/alpine-miniconda3 as builder
COPY . /app
RUN conda env create --file app/environment.yml -p /env

FROM frolvlad/alpine-miniconda3
EXPOSE 5000
COPY --from=builder /env /env
COPY --from=builder /app /app
WORKDIR /app
CMD source activate /env && python run.py
