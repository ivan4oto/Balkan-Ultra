<template>
    <div>
      <b-container class='mt-4'>

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
        <h1 class='mt-4'><strong>"Само при мисълта за старт на Балкан ултра ми се изпотяват дланите."</strong></h1>
        <h4>-Калоян Кофе Пейчев</h4>
        <!-- <h1 class='mt-4'><strong>"UTMB носи точки за Балкан Ултра!"</strong></h1>
        <h4>-Иван Гочев</h4> -->
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
@media only screen and (max-width: 375) {
  h1 {
    font-size: 15px;
    color: rgb(136, 4, 4);
  }
}
h1 {
  font-size: 60px;
  font-weight: bolder;
  color: rgb(136, 4, 4);
}
</style>
