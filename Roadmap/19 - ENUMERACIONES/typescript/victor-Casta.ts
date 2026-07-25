enum DaysOfTheWeek {
  MONDAY = 1,
  TUESDAY = 2,
  WEDNESDAY = 3,
  THURSDAY = 4,
  FRIDAY = 5,
  SATURDAY = 6,
  SUNDAY = 7
}

const getDay: (number: number) => string  = (number: number) => {
  return DaysOfTheWeek[number]
}

console.log(getDay(1))


/*
  * Extra
*/


enum DeliveryStatus {
  PENDING,
  SHIPPED,
  DELIVERED,
  CANCELLED
}

class OrderSystem {
  id: number
  status: DeliveryStatus
  nameOfOrder: string

  constructor(id: number, nameOfOrder: string) {
    this.id = id
    this.status = DeliveryStatus.PENDING
    this.nameOfOrder = nameOfOrder
  }

  orderShipped() {
    if (this.status !== DeliveryStatus.PENDING) {
      console.log(`El pedido "${this.nameOfOrder}" ya se ha enviado o cancelado`)
      return
    }
    this.status = DeliveryStatus.SHIPPED
    console.log(`El pedido "${this.nameOfOrder}" ha sido enviado`)
  }

  orderCancelled() {
    if (this.status === DeliveryStatus.SHIPPED) {
      console.log(`El pedido "${this.nameOfOrder}" no se puede cancelar porque ya se ha enviado`)
      return
    }
    if (this.status === DeliveryStatus.CANCELLED) {
      console.log(`El pedido "${this.nameOfOrder}" ya se encuentra cancelado`)
      return
    }
    if (this.status === DeliveryStatus.DELIVERED) {
      console.log(`El pedido "${this.nameOfOrder}" no se puede cancelar porque ya se ha entregado`)
      return
    }
    this.status = DeliveryStatus.CANCELLED
    console.log(`El pedido "${this.nameOfOrder}" ha sido cancelado`)
  }

  orderDelivered() {
    if (this.status === DeliveryStatus.CANCELLED) {
      console.log(`El pedido "${this.nameOfOrder}" no se puede entregar porque ha sido cancelado`)
      return
    }
    if (this.status === DeliveryStatus.PENDING) {
      console.log(`El pedido "${this.nameOfOrder}" aún no se ha enviado`)
      return
    }
    this.status = DeliveryStatus.DELIVERED
    console.log(`El pedido "${this.nameOfOrder}" ha sido entregado`)
  }

  actualStateOfOrder() {
    const statusMap = {
      [DeliveryStatus.PENDING]: 'Pendiente',
      [DeliveryStatus.SHIPPED]: 'Enviado',
      [DeliveryStatus.DELIVERED]: 'Entregado',
      [DeliveryStatus.CANCELLED]: 'Cancelado'
    }
    console.log(`El estado actual del pedido "${this.nameOfOrder}" es: ${statusMap[this.status]}`)
  }
}

const burguerOrder = new OrderSystem(1, 'Burguer Max')
burguerOrder.actualStateOfOrder()
burguerOrder.orderShipped()
burguerOrder.actualStateOfOrder()
burguerOrder.orderDelivered()
burguerOrder.actualStateOfOrder()

const iceCreamOrder = new OrderSystem(2, 'Ice cream')
iceCreamOrder.actualStateOfOrder()
iceCreamOrder.orderShipped()
iceCreamOrder.orderCancelled()
iceCreamOrder.actualStateOfOrder()
iceCreamOrder.orderDelivered()
iceCreamOrder.actualStateOfOrder()