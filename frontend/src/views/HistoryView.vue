<template>
  <div class="history">
    <History />
  </div>
</template>

<script>
// @ is an alias to /src
import History from "@/components/History.vue";

export default {
  name: "HistoryView",
  components: {
    History,
  },
};
</script>
