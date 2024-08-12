import React from "react";
import { mainCarouselData } from "./MainCarouselData";
import AliceCarousel from "react-alice-carousel";
import "react-alice-carousel/lib/alice-carousel.css";



const MainCarousel = () => {
  const items = mainCarouselData.map((items) => (
    // <div style={{ backgroundColor: 'blue', padding: '20px', color: 'white' }}>
      <img
        className="cursor-pointer -z-10 my-class"
        role="presentation"
        src={items.image}
        alt=""
        // style={{ objectFit: "cover" }}
      />
    // </div>
  ));

  return (
    <AliceCarousel
      items={items}
      disableButtonsControls
       autoPlay
       autoPlayInterval={2000}
      infinite
    />
  );
};

export default MainCarousel;
