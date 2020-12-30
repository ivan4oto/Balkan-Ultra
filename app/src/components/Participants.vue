<template>
  <div class="m-3">
    <b-card
      overlay
      img-src="../assets/pictures/participants-banner.jpg"
      img-alt="Card Image"
      text-variant="white"
      class='text-center'
      title=""
      sub-title=""
    >
    <b-card-text id='card-txt'>
     РЕГИСТРИРАНИ УЧАСТНИЦИ
    </b-card-text>
    </b-card>
        <b-table
          striped
          table-variant: dark
          responsive
          small
          hover
          :items="athletes"
          :fields="fields"
        ></b-table>
  </div>
</template>
<script>
const axios = require("axios").default;

export default {
  name: "Participants",
  data() {
    return {
      testvam: null,
      fields: [
        {
          key: "first_name",
          label: "Име",
          sortable: false
        },
        {
          key: "last_name",
          label: "Фамилия",
          sortable: false,
        },
        {
          key: "gender",
          label: "Пол",
          sortable: true,
          // Variant applies to the whole column, including the header and footer
          variant: "",
        },
        {
          key: "distance",
          label: "Трасе",
          sortable: true,
        },
      ],
      athletes: [],
    };
  },
  methods: {
    getAthletes() {
      axios
        .get(this.api_uri['athlete'])
        .then((response) => {
          console.log(response.data);
          this.athletes = response.data;
        })
        .catch(function(error) {
          console.log(error);
        })
        .then(function (){
            // always executed
        });
    },
  },
  mounted: function() {
    this.getAthletes()
    console.log("mounted");
  },
};
</script>

<style scoped>
.frame {
  border: 5px solid rgb(34, 60, 87);
}
#card-txt{
  font-family: 'SPArielBG';
  font-weight: normal;
  color: rgb(199, 224, 87);
}
@media screen and (min-width: 320px) {
  #card-txt {
    font-size: 5vw;
  }
}
@media screen and (min-width: 768px) {
  #card-txt {
    font-size: 5vw;
  }
}
@media screen and (min-width: 1000px) {
  #card-txt {
    font-size: 3vw;
  }
}

</style>