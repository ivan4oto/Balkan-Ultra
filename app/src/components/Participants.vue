<template>
  <div class="m-3">
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
          sortable: false
        },
        {
          key: "last_name",
          sortable: false,
        },
        {
          key: "gender",
          sortable: true,
          // Variant applies to the whole column, including the header and footer
          variant: "",
        },
        {
          key: "distance",
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
          console.log(response.status);
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
</style>