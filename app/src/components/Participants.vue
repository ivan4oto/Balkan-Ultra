<template>
  <div class="m-3">
    <div id="img-test">
      <h2>РЕГИСТРИРАНИ УЧАСТНИЦИ</h2>
    </div>
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

#img-test {
    background-image:url("../assets/pictures/participants-banner.jpg");
    background-position:center;
    padding-top: 5%;
    padding-bottom: 5%;
    color: rgb(235, 231, 12);
    text-align: center;
}

</style>