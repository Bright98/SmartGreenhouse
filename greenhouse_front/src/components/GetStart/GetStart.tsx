import React from "react";
import { ChevronsDown } from "react-feather";

const GetStart: React.FC = () => {
  return (
    <div className="getStart">
      <div className="getStart__top">
        <div className="col-lg-7 getStart__top__right">
          <div className="getStart__top__right__title">گلخانه هوشمند</div>
          <div className="getStart__top__right__screen">
            <p>
              آبیاری گل و گیاهان یکی از مشکلات همیشگیه که ممکن یادمون بره و
              گیاهامون آسیب ببینن... یکی از راه حل هایی که میشه براش درنظر گرفت
              آبیاری خودکار اونهاست. به کمک این سایت میتونیم گیاهامونو از راه
              دور آبیاری کنیم درواقع میتونیم گلخونه ای داشته باشیم که وضعیت
              آبیاری گلها، تهویه هوای گلخونه و دما و رطوبت رو از راه دورکنترل
              کنیم.
            </p>
          </div>
        </div>

        <div className="col-lg-5 getStart__top__left">
          <img
            src={require("../../assets/flat_icons/wifi.svg")}
            className="getStart__top__left__wifi"
          />
          <img
            src={require("../../assets/flat_icons/greenhouse.svg")}
            className="getStart__top__left__greenhouse"
          />
        </div>
      </div>

      <div className="getStart__bottom">
        <a className="getStart__bottom__scrollButton" href="#content">
          <ChevronsDown />
        </a>
      </div>
    </div>
  );
};

export default GetStart;
