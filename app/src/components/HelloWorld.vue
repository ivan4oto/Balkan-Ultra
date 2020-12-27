<template>
    <div>
        <b-carousel
          id="carousel-fade"
          style="text-shadow: 0px 0px 2px #000"
          fade
          indicators
          img-width="1024"
          img-height="480"
        >
          <b-carousel-slide
            caption=""
            img-src="../assets/pictures/c1.jpg"
          ></b-carousel-slide>
          <b-carousel-slide
            caption=""
            img-src="../assets/pictures/c2.jpg"
          ></b-carousel-slide>
          <b-carousel-slide
            caption=""
            img-src="../assets/pictures/c3.jpg"
          ></b-carousel-slide>
        </b-carousel>
        <b-row>
          
          <b-col sm>
            <b-card
              overlay
              img-src="../assets/pictures/main-1.jpg"
              img-alt="Card Image"
              text-variant="white"
              class=''
              title=""
              sub-title=""
            >
              <h4 id='txt-1'>Балкан Ултра е състезание по планинско бягане, което се провежда в началото на Август месесц в Централен Балкан. Дължината на трасето е 80км, като от тази година имаме ново трасе, 13км. И двете трасета са по стръмен планински терен, изцяло по планински пътеки и с участъци с висока техническа трудност.</h4>
            </b-card>
          </b-col>
          <b-col sm>
            <b-card
              overlay
              img-src="../assets/pictures/main-2.jpg"
              img-alt="Card Image"
              text-variant="white"
              class='text-right'
              title=""
              sub-title=""
            >
              <h4 id='txt-2'>Трасето минава през 6 хижи и 10 контролни пункта. Нужна е висока физическа подготовка, опит в планината и воля, за успешно завършване на Балкан Ултра. Контролното време на състезанието е 20 часа за трасе 80км.</h4>
            </b-card>
          </b-col>
        </b-row>

        <b-container class='mt-2'>
        <b-embed
          type="iframe"
          aspect="16by9"
          src="https://www.youtube.com/embed/zaJccw5h5P4"
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
              <h3 id='txt-kofe-2'>- Калоян Пейчев (победител от 2020г)</h3>
            
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
              <h2 id='txt-pirin'>Има два вида ултрамаратонци, такива, които обожават Балкан Ултра, и такива които нямат вкус!</h2>
              <h3 id='txt-pirin-2'>- Пирин Галов</h3>
              <h3 id='txt-pirin-2'>(машина от 1974г.)</h3>
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

@media (max-width: 767px) {
  h1 {
   font-size: 20px;
   font-family: 'Roboto', sans-serif;
  }
  h4 {
    font-size: 18px;
    font-family: 'Roboto', sans-serif;
  }
  h2 {
    font-size: 20px;
  }
  h3 {
    font-size: 20px;
  }
}

h4 {
  font-family: 'SPArielBG';
  font-weight: bold;
}
#txt-1{
  font-weight: bold;
  font-style: italic;
  color: rgb(12, 44, 92);
}
#txt-2{
  font-weight: bold;
  font-style: italic;
  color: rgb(12, 44, 92);
}
#txt-kofe{
  font-weight: bold;
  font-style: italic;
  color: rgb(184, 28, 8);
}
#txt-kofe-2{
  font-weight: bold;
  font-style: italic;
  color: rgb(121, 17, 3);
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
</style>
