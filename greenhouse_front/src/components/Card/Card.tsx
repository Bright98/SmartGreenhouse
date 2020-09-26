import React from "react";

interface cardProps {
  children: React.ReactNode;
}

const Card: React.FC<cardProps> = ({ children }) => {
  return (
    <div className="card">
      <div className="card__body">{children}</div>
    </div>
  );
};

export default Card;
