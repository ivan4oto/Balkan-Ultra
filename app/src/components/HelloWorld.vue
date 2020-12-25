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
          <b-col sm><b-img src="../assets/pictures/main-1.jpg" fluid alt="Fluid image"></b-img></b-col>
          <b-col sm><b-img src="../assets/pictures/main-2.jpg" fluid alt="Fluid image"></b-img></b-col>
        </b-row>
        <b-container class='mt-2'>
        <b-embed
          type="iframe"
          aspect="16by9"
          src="https://www.youtube.com/embed/zaJccw5h5P4"
          allowfullscreen
        ></b-embed>
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
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
@media (max-width: 767px) {
  h1 {
   font-size: 20px;
   font-family: 'Roboto', sans-serif;
  }
  h4 {
    font-size: 15px;
    font-family: 'Roboto', sans-serif;
  }
}


</style>
