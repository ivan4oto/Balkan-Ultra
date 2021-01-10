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
        <b-carousel-slide img-src="../assets/pictures/crsl1.jpg">
          <h1>78 км с 6100м д+ по склоновете на Стара Планина!</h1>
        </b-carousel-slide>
        <!-- Slides with image only -->
        <b-carousel-slide img-src="../assets/pictures/c2.jpg">
        </b-carousel-slide>
      </b-carousel>
      <b-container>
        <div id='bglight' class='m-3'>
          <b-row>
            <b-col>
              <h3 class='redheader'>Какво е Балкан Ултра?</h3>
              <p>Балкан Ултра е състезание по планинско бягане, което се провежда в началото на месец август в Централен Балкан. Дължината на маршрута е 78 км, като от тази година имаме ново късо трасе с дължина 13.5 км. И двете трасета са по стръмен планински терен, изцяло по планински пътеки и  участъци с <strong>висока техническа трудност.</strong></p>
            </b-col>
            <b-col>
            <h3 class='redheader'>Най-голям процент DNF'и!</h3>
            <p>От <strong>35 стартирали</strong> участника през 2020 г., <strong>едва 14</strong> от тях успяха да се приберат в контролното време от 20 часа. Мнозина подцениха трасето и надцениха своите възможности. Дори и най-закоравелите ултрамаратонци се огъват под натиска на Балкана. Готов ли си да се впуснеш в едно наистина истинско предизвикателство? </p>
            </b-col>
          </b-row>
        </div>
      </b-container>
      <b-container class='mb-3'>
        <b-row>
          <b-img fluid alt="Fluid image" src='../assets/pictures/wildcard.jpg'>
          </b-img>
        </b-row>
        <b-row class='text-center'>
          <h2 id='txt-wildcard'>Петима, които желаят да се състезават, но не покриват изискванията за участие, ще получат Wild Card за Балкан Ултра 2021.</h2>
          <p id='txt-wildcard-small'>За да се сдобиете с Wild Card трябва да покажете силно желание за участие в Балкан Ултра. Всякакви планински изпълнения като 5 поредни изкачвания на Черни връх или тренировъчно минаване на трасето на Балкан Ултра ще бъдат приети  като потенциални кандидатури. Подкупи отправени към организаторите под формата на зимнина и други консумативи с домашен произход могат да наклонят везните при евентуално обсъждане на даден кандидат.</p>
        </b-row>
      </b-container>

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
</style>
