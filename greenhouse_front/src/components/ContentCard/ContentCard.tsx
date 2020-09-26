import React, { ReactNode } from "react";

interface cardProps {
  title: string;
  number: string;
  number_sign?: string;
  children?: ReactNode;
  image1: string;
  image2: string;
}

const ContentCard: React.FC<cardProps> = ({
  title,
  number,
  number_sign,
  children,
  image1,
  image2
}) => {
  return (
    <div className="contentCard">
      <div className="contentCard__title">
        <span>{title}</span>
        <div className="contentCard__title__image">
          <img
            src={require("../../assets/flat_icons/" + `${image1}` + ".svg")}
            className="contentCard__title__image__image1"
            alt={"image1"}
          />
          <img
            src={require("../../assets/flat_icons/" + `${image2}` + ".svg")}
            className="contentCard__title__image__image2"
            alt={"image2"}
          />
        </div>
      </div>
      <div className="contentCard__number">
        <span>{number}</span>
        <span>{number_sign}</span>
        {children}
      </div>
    </div>
  );
};

export default ContentCard;
