import React from 'react'
import MainCarousel from '../../components/HomeCarousel/MainCarousel'
import HomeSectionCarousel from '../../components/HomeSectionCarousel/HomeSectionCarousel'
import { movieData } from '../../../data/movieData'

const HomePage = () => {
  return (
    <div>
        <MainCarousel/>

        <div className='space-y-10 py-20 flex flex-col justify-center px-5 lg:px-10'>
            <HomeSectionCarousel data={movieData} sectionName={"Movies"}/>
            <HomeSectionCarousel data={movieData} sectionName={"Series"}/>
            <HomeSectionCarousel data={movieData} sectionName={"Hehe"}/>
        </div>
    </div>
  )
}

export default HomePage