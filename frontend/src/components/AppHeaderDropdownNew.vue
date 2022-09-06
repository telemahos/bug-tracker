<template>
  <CDropdown variant="nav-item">
    <CDropdownToggle placement="bottom-end" class="py-0" :caret="true">
      <CAvatar size="md" /><CBadge color="info" class="ms-auto">New +</CBadge>
    </CDropdownToggle>
    <CDropdownMenu class="pt-0">
      <CDropdownHeader component="h6" class="bg-light fw-semibold py-2">
        Create new:
      </CDropdownHeader>
      <CDropdownItem>
        <CIcon icon="cil-task" />
        <CNavLink href="#/theme/ticketlist">New Ticket</CNavLink>
        <!-- <CBadge color="info" class="ms-auto">+</CBadge> -->
      </CDropdownItem>
      <CDropdownItem>
        <CIcon icon="cil-puzzle" />
        <CNavLink href="#/theme/project">New Project</CNavLink>
        <!-- <CBadge color="success" class="ms-auto">{{ itemsCount }}</CBadge> -->
      </CDropdownItem>
      <CDropdownItem>
        <CIcon icon="cil-envelop" />
        <CNavLink href="#/theme/inbox">New Message</CNavLink>
        <!-- <CBadge color="danger" class="ms-auto">{{ itemsCount }}</CBadge> -->
      </CDropdownItem>
      <CDropdownItem>
        <CIcon icon="cil-envelope-open" /> New Message cil-account-logout
        <!-- <CBadge color="warning" class="ms-auto">{{ itemsCount }}</CBadge> -->
      </CDropdownItem>
    </CDropdownMenu>
  </CDropdown>
</template>

<script>
import images from '@/assets/images/vue.jpg'

export default {
  name: 'AppHeaderDropdownNew',
  setup() {
    return {
      the_image: images,
      itemsCount: 42,
    }
  },
}
</script>
