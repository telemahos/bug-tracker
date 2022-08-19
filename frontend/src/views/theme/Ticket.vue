<template>
  <h1>This is Ticket Page!</h1>
  <a href="/AddTicket">Add Ticket</a><br />

  <CLink :href="AddTicket"> Add Ticket 2 </CLink>
</template>

<script>
export default {
  name: 'Ticket',
}
</script>
