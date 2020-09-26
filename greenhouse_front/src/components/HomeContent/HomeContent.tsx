import React, { useState, useEffect } from "react";
import { Card, ContentCard } from "../index";
import { Percent } from "react-feather";
import axios from "axios";

const HomeContent: React.FC = () => {
  const [item, setItems] = useState();
  const [watering, setWater] = useState();
  const [fan, setFan] = useState();

  useEffect(() => {
    const interval1 = setInterval(
      () =>
        axios.get("http://localhost:8000/dht_sensor/").then(res => {
          setItems(res.data);
        }),
      5000
    );
    const interval2 = setInterval(
      () =>
        axios.get("http://localhost:8000/watering/").then(res => {
          setWater(res.data);
        }),
      5000
    );
    const interval3 = setInterval(
      () =>
        axios.get("http://localhost:8000/fan/").then(res => {
          setFan(res.data);
        }),
      5000
    );
    return () => {
      clearInterval(interval1);
      clearInterval(interval2);
      clearInterval(interval3);
    };
  }, []);

  const HandleWatering = () => {
    const qs = require("query-string");

    axios
      .post(
        "http://localhost:8000/watering/",
        qs.stringify({
          water_request: "True"
        }),
        qs.stringify({
          "content-type": "application/json"
        })
      )
      .then(res => {
        console.log(res.data);
      })
      .catch(error => {
        console.log(error);
      });
  };

  const HandleFan = () => {
    const qs = require("query-string");

    axios
      .post(
        "http://localhost:8000/fan/",
        qs.stringify({
          fan_request: "True"
        }),
        qs.stringify({
          "content-type": "application/json"
        })
      )
      .then(res => {
        console.log(res.data);
      })
      .catch(error => {
        console.log(error);
      });
  };

  return (
    <div className="homeContent" id="content">
      <div className="homeContent__row">
        <div className="col-lg-6 homeContent__row__temperature">
          <Card>
            <ContentCard
              title="دما"
              number={item !== undefined ? item.temperature : "0"}
              number_sign="&deg;"
              image1="thermometer"
              image2="snow"
            />
          </Card>
        </div>

        <div className="col-lg-6 homeContent__row__humidity">
          <Card>
            <ContentCard
              title="رطوبت"
              number={item !== undefined ? item.humidity : "0"}
              image1="water"
              image2="wind"
            >
              <Percent />
            </ContentCard>
          </Card>
        </div>
      </div>

      <div className="homeContent__row">
        <div className="col-md-6 homeContent__row__watering">
          <Card>
            <ContentCard
              title="آبیاری"
              number="آخرین بروز رسانی: "
              number_sign={
                "ساعت " +
                `${watering !== undefined ? watering.watering_hour : "0"}` +
                ":" +
                `${watering !== undefined ? watering.watering_minute : "0"}` +
                " - " +
                "تاریخ " +
                `${watering !== undefined ? watering.watering_month : "0"}` +
                "/" +
                `${watering !== undefined ? watering.watering_day : "0"}` +
                "/"
              }
              image1="watering-can"
              image2="water-drop"
            >
              <div className="homeContent__row__button">
                <button onClick={HandleWatering}>آبیاری</button>
              </div>
            </ContentCard>
          </Card>
        </div>

        <div className="col-md-6 homeContent__row__fan">
          <Card>
            <ContentCard
              title="تهویه هوا"
              number="آخرین بروز رسانی: "
              number_sign={
                "ساعت " +
                `${fan !== undefined ? fan.fan_hour : "0"}` +
                ":" +
                `${fan !== undefined ? fan.fan_minute : "0"}` +
                " - " +
                "تاریخ " +
                `${fan !== undefined ? fan.fan_month : "0"}` +
                "/" +
                `${fan !== undefined ? fan.fan_day : "0"}` +
                "/"
              }
              image1="fan"
              image2="fan-wind"
            >
              <div className="homeContent__row__button">
                <button onClick={HandleFan}>تهویه هوا</button>
              </div>
            </ContentCard>
          </Card>
        </div>
      </div>
    </div>
  );
};

export default HomeContent;
