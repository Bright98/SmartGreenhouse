import React from "react";
import { GetStart, HomeContent } from "../../components/index";

const Home: React.FC = () => {
  return (
    <div className="home">
      <GetStart />
      <HomeContent />
    </div>
  );
};

export default Home;
