<template>
  
  <h1 class="mb-8">
    Ticket details!
    <small class="text-muted">Bugs</small>
  </h1>
  

  <CRow>
    <CCol :xs="12">
      <!-- <DocsCallout name="Badges" href="components/badge.html" />-->
    </CCol>
    <CCol :lg="4">
      <CCard class="mb-4">
        <CCardHeader> <strong></strong> <small>DETAILS</small> </CCardHeader>
        <CCardBody>
          <CListGroup>
            <CListGroupItem
              class="d-flex justify-content-between align-items-center"
            >
              Case No.
              <small>070922-N073</small>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Title</h6>
                <small>Bug in Login and Logout</small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Project</h6>
                <small>Project Title 3</small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Type</h6>
                <small class="text-dark">Bug</small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Priority</h6>
                <CBadge color="danger">Critical</CBadge>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Status</h6>
                <small class="text-info">In Progress</small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Due Date</h6>
                <small>Sep 28, 2022</small>
              </div>
            </CListGroupItem>
          </CListGroup>
        </CCardBody>
      </CCard>
      <CCard class="mb-4">
        <CCardHeader>
          <strong></strong> <small>ASSIGNED TO</small>
        </CCardHeader>
        <CCardBody>
          <CListGroup>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between align-items-center">
                <h6 class="mb-1">Owner</h6>
                <!-- <CAvatar 
                  size="md" 
                  :src="avatar.src"
                  :status="avatar.status"/>         -->
                <small>
                  Konstantinos Kakoulis<br /><span class="text-muted"
                    >Web Devloper</span
                  ></small
                >
              </div>
            </CListGroupItem>
          </CListGroup>
        </CCardBody>
      </CCard>
    </CCol>
    <CCol :lg="8">
      <CCard class="mb-4">
        <CCardHeader>
          <strong></strong> <small>DESCRIPTION</small>
        </CCardHeader>
        <CCardBody>
          <p class="text-medium-emphasis small">
            It will be as simple as occidental in fact, it will be Occidental.
            To an English person, it will seem like simplified English, as a
            skeptical Cambridge friend of mine told me what Occidental is. The
            European languages are members of the same family. Their separate
            existence is a myth. For science, music, sport, etc, Europe uses the
            same vocabulary. The languages only differ in their grammar, their
            pronunciation and their most common words.
          </p>
        </CCardBody>
      </CCard>
      <CCard class="mb-4">
        <CCardHeader> <strong></strong> <small>COMMENTS</small> </CCardHeader>
        <CCardBody>
          
          <CCard class="">
            <CCardBody>
              <!-- <CCardTitle>Card title</CCardTitle> w-75-->
              <CCardSubtitle>Kakoulis Kostas <small class="text-muted">20 Dec 2021 - 05:47AM</small></CCardSubtitle>
              <CCardText>
                <p class="text-medium-emphasis small">I am getting message from customers that when they place order always get error message .</p>
                <!-- <p><CCardLink>Edit</CCardLink></p> -->
              </CCardText>
              <!-- <CButton href="#">Go somewhere</CButton> -->
            </CCardBody>
          </CCard>
          <CCard class="">
            <CCardBody>
              <!-- <CCardTitle>Card title</CCardTitle> w-75-->
              <CCardSubtitle>Panagiotidou Noula <small class="text-muted">20 Dec 2021 - 05:47AM</small></CCardSubtitle>
              <CCardText>
                <p class="text-medium-emphasis small">I am getting message from customers that when they place order always get error message .</p>
                <p><CCardLink>Edit</CCardLink></p>
              </CCardText>
              <!-- <CButton href="#">Go somewhere</CButton> -->
            </CCardBody>
          </CCard>


        </CCardBody>
      </CCard>
    </CCol>
  </CRow>
</template>

<script>
import avatar from '@/assets/images/avatars/2.jpg'
export default {
  name: 'ticketdetails',
  setup() {
    return {
      // avatar: avatar,
      avatar: { src: avatar, status: 'success' },
    }
  },
}
</script>
