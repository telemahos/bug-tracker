### REPORT ###

--- When I call via SQL many row.sall(), then I have to do List[schema.tableModel], otherwise row.first(), must be simple schema.tableModel and not list
--- On an error 422 on API call, check if send correct data, e.g. String as String or integer as integer. Copy a call Example Value Schema from Swager and compare it to the data that the application is sending. You may send wrong data types 
--- When I have an object and I want to turn it into a prop, then I can add some other properties, enrich it with more data and passed it to a component
<div v-bind:the_case="the_case.projectOwner = userNames[index]">{{ userNames[index] }}</div>
--- Call a parent function from child component: 
Parent: <AppOffcanvasTicketEdit @updateTicketList="(event) => loadTicket()" />
Child:  <CButton color="primary" type="submit" @click="$emit('updateTicketList')">Submit</CButton
--- 