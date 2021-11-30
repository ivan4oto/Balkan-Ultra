<template>
    <div>
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
        background="#ababab"
        img-width="1024"
        img-height="480"
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <b-carousel-slide img-src="../assets/pictures/c1.jpg"></b-carousel-slide>
        <!-- Slides with custom text -->
        <b-carousel-slide img-src="../assets/pictures/c5.jpg">
          <h1></h1>
        </b-carousel-slide>
        <!-- Slides with image only -->
        <b-carousel-slide img-src="../assets/pictures/c2.jpg">
        </b-carousel-slide>
                <b-carousel-slide img-src="../assets/pictures/crsl1.jpg">
          <h1>78 км с 6100м д+</h1>
          <h1>и 13 км с 1700м д+ по склоновете на Стара Планина!</h1>
        </b-carousel-slide>
      </b-carousel>
      <div id='bglight' class='mt-2'>
        <b-container class='mb-3'>
          
            <ul class='text-center lightbox'>
              <b-row class='text-center'>
                  <b-col>
                  <h3 class='blueheader'>Програма на състезанието:</h3>
                  </b-col>
              </b-row>
              <b-col>
                <b-row class='text-left'>
                    <li class='orangeli m-2'>Петък, 6 август:</li>
                </b-row>
                <b-row class='text-left m-1'>
                    <p><i>Взимане на стартовата гривна и GPS устройство:</i> Целият ден до 23:00 ч. вечерта срещу валидна планинска застраховка (копие на застрахователната полица или показването на документа през телефона) и задължителната екипировка.</p>
                    <p><i>Вечеря:</i> След 19:00 ч. ще бъде сервирана безплатна вечеря за участниците. Вечерята ще бъде без животински продукти, като от хижата може да си поръчате допълнително пържолки, кюфтенца и други неща.</p>
                    <p><i>Техническа конференция:</i> От 21:00 ч. в "залата с пианото" на първия етаж на хижата. Ще съобщим метеорологичната прогноза, накратко за трасето и ще отговаряме на вашите въпроси.</p>
                </b-row>
                <b-row class='text-left'>
                    <li class='orangeli m-2'>Събота, 7 август:</li>
                </b-row>
                <b-row class='text-left m-1'>
                    <p><i>Старт на дългата дистанция:</i> В 05:40 ч. на поляната пред хижа Плевен. Бъдете там поне 15-20 минути по-рано. На място ще се проверява допълнително задължителната екипировка на всички участници.</p>
                    <p><i>Старт на късата дистанция:</i> В 08:30 ч. на поляната пред хижа Плевен.</p>
                    <p><i>Награждаване на късата дистанция:</i> В 15:00 ч. на поляната зад хижа Плевен.</p>
                    <p><i>Очакване на победителите на дългата дистанция:</i> След 17:00 часа.</p>
                </b-row>
                <b-row class='text-left'>
                    <li class='orangeli m-2'>Неделя, 8 август:</li>
                </b-row>
              <b-row class='text-left m-1'> 
                    <p><i>Край на контролно време:</i> 01:40 ч.</p>
              </b-row>
              <b-row class='text-left m-1'>
                    <p><i>Награждаване на дълга дистанция:</i> 10:00 ч. на поляната зад хижа Плевен.</p>   
              </b-row>         

              </b-col>
             </ul>
      
        </b-container>
      </div>
        <b-container class='mt-2'>
        <b-embed
          type="iframe"
          aspect="16by9"
          src="https://www.youtube.com/embed/A5hWDl1Gtls"
          allowfullscreen
        ></b-embed>
        </b-container>
        <b-container>
          <b-row>
          
          <b-col sm>
            <b-card
              overlay
              img-src="../assets/pictures/kofebw.jpg"
              img-alt="Card Image"
              text-variant="white"
              class=''
              title=""
              sub-title=""
            >
           
              <h2 id='txt-kofe'>Само при мисълта за старт на Балкан ултра ми се изпотяват дланите.</h2>
              <h3 id='txt-kofe-2'>- Калоян Пейчев (победител от 2020 г.)</h3>
            
            </b-card>
          </b-col>
          <b-col sm>
            <b-card
              overlay
              img-src="../assets/pictures/pirinbw.jpg"
              img-alt="Card Image"
              text-variant="white"
              class='text-left'
              title=""
              sub-title=""
            >
              <h2 id='txt-pirin'>Има два вида ултрамаратонци - такива, които обожават Балкан Ултра, и такива, които нямат вкус!</h2>
              <h3 id='txt-pirin-2'>- Пирин Галов</h3>
              <h3 id='txt-pirin-2'>(машина от 1974 г.)</h3>
            </b-card>
          </b-col>
        </b-row>
        </b-container>
    </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {},
  data() {
    return {
      slide: 0,
      sliding: null,
    };
  },
  methods: {
    onSlideStart() {
      this.sliding = true;
    },
    onSlideEnd() {
      this.sliding = false;
    },
  },
};
</script>

<style scoped>
p, h4, h1, h2, h3{
  font-family: 'SPArielBG';
}
@media (max-width: 767px) {
  h1 {
   font-size: 20px;
  }
  h4 {
    font-size: 18px;
  }
  h2 {
    font-size: 20px;
  }
  h3 {
    font-size: 20px;
  }
}

h4 {
  font-weight: bold;
}
#txt-1{
  font-weight: normal;
  color: rgb(0, 0, 0);
}
#txt-2{
  font-weight: normal;
  color: rgb(0, 0, 0);
}
#txt-kofe{
  font-weight: bold;
  font-style: italic;
  color:rgb(247, 216, 44);
}
#txt-kofe-2{
  font-weight: bold;
  font-style: italic;
  color: rgb(224, 184, 50);
}
#txt-pirin{
  font-weight: bold;
  font-style: italic;
  color: rgb(247, 216, 44);
}
#txt-pirin-2{
  font-weight: bold;
  font-style: italic;
  color: rgb(224, 184, 50);
}
#txt-wildcard{
  font-weight: bold;
  color: rgb(189, 27, 6);
}
#txt-wildcard-small{
  font-style: italic;
  color: rgb(10, 10, 10);
}
.redheader {
  font-weight: bold;
  color: rgb(189, 27, 6);
}
.blueheader {
  font-weight: bold;
  color: rgb(20, 50, 88);
}

ul {
  list-style-type: none;
  border: 1px solid lightskyblue;
  margin: 0;
  padding: 0;
}

.orangeli {
  color: orangered;
}
</style>
