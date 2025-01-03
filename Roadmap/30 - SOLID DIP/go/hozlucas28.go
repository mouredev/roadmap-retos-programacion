package main

import (
	"fmt"
)

/* -------------------------------------------------------------------------- */
/*                                 INTERFACES                                 */
/* -------------------------------------------------------------------------- */

type CreditCardPayment interface {
	Process()
}

type BadPaymentProcessor interface {
	Process()
}

type PayPalPayment interface {
	Process()
}

type PaymentMethod interface {
	Process()
}

type GoodPaymentProcessor interface {
	Process()
}

type NotificationService interface {
	Send()
}

type NotificationSystem interface {
	SendNotification()
}

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* ---------------------------- CreditCardPayment --------------------------- */

type creditCardPayment struct{}

func NewCreditCardPayment() CreditCardPayment {
	var creditCardPayment creditCardPayment = creditCardPayment{}
	return &creditCardPayment
}

func (creditCardPayment *creditCardPayment) Process() {
	fmt.Println("Credit card payment processed!")
}

/* --------------------------- BadPaymentProcessor -------------------------- */

type badPaymentProcessor struct {
	method creditCardPayment
	_      struct{}
}

func NewBadPaymentProcessor() BadPaymentProcessor {
	var paymentProcessor badPaymentProcessor = badPaymentProcessor{
		method: creditCardPayment{},
	}

	return &paymentProcessor
}

func (paymentProcessor *badPaymentProcessor) Process() {
	paymentProcessor.method.Process()
}

/* ------------------------------ PayPalPayment ----------------------------- */

type payPalPayment struct{}

func NewPayPalPayment() PayPalPayment {
	var payPalPayment payPalPayment = payPalPayment{}
	return &payPalPayment
}

func (payPalPayment *payPalPayment) Process() {
	fmt.Println("PayPal payment processed!")
}

/* -------------------------- GoodPaymentProcessor -------------------------- */

type goodPaymentProcessor struct {
	method PaymentMethod
	_      struct{}
}

func NewGoodPaymentProcessor(method PaymentMethod) GoodPaymentProcessor {
	var paymentProcessor goodPaymentProcessor = goodPaymentProcessor{
		method: method,
	}

	return &paymentProcessor
}

func (paymentProcessor *goodPaymentProcessor) Process() {
	paymentProcessor.method.Process()
}

/* ------------------------------ EmailService ------------------------------ */

type emailService struct{}

func NewEmailService() NotificationService {
	var emailService emailService = emailService{}
	return &emailService
}

func (emailService *emailService) Send() {
	fmt.Println("Email sent!")
}

/* ------------------------------- PushService ------------------------------ */

type pushService struct{}

func NewPushService() NotificationService {
	var pushService pushService = pushService{}
	return &pushService
}

func (pushService *pushService) Send() {
	fmt.Println("Push sent!")
}

/* ------------------------------- SMSService ------------------------------- */

type smsService struct{}

func NewSMSService() NotificationService {
	var smsService smsService = smsService{}
	return &smsService
}

func (smsService *smsService) Send() {
	fmt.Println("SMS sent!")
}

/* --------------------------- NotificationService -------------------------- */

type notificationSystem struct {
	notificationService NotificationService
}

func NewNotificationSystem(notificationService NotificationService) NotificationSystem {
	var notificationSystem notificationSystem = notificationSystem{notificationService: notificationService}
	return &notificationSystem
}

func (notificationSystem *notificationSystem) SendNotification() {
	notificationSystem.notificationService.Send()
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		Dependency Inversion Principle (DIP)...
	*/

	fmt.Println("Dependency Inversion Principle (DIP)...")

	fmt.Println("\nBad implementation of Dependency Inversion Principle (DIP)...")

	fmt.Println("\n```\n" + `type CreditCardPayment interface {
  Process()
}

type BadPaymentProcessor interface {
  Process()
}

type creditCardPayment struct{}

func NewCreditCardPayment() CreditCardPayment {
  var creditCardPayment creditCardPayment = creditCardPayment{}
  return &creditCardPayment
}

func (creditCardPayment *creditCardPayment) Process() {
  fmt.Println("Credit card payment processed!")
}

type badPaymentProcessor struct {
  method creditCardPayment
  _      struct{}
}

func NewBadPaymentProcessor() BadPaymentProcessor {
  var paymentProcessor badPaymentProcessor = badPaymentProcessor{
    method: creditCardPayment{},
  }

  return &paymentProcessor
}

func (paymentProcessor *badPaymentProcessor) Process() {
  paymentProcessor.method.Process()
}` + "\n```")

	fmt.Println(
		"\nThis is a bad implementation of Dependency Inversion Principle (DIP),\n" +
			"'badPaymentProcessor' class depends directly on the 'creditCardPayment' class\n" +
			"rather than on an interface. So, if the 'method' attribute in the 'badPaymentProcessor'\n" +
			"class needs to be changed, the constructor ('NewBadPaymentProcessor') must also be modified.",
	)

	fmt.Println("\nGood implementation of Dependency Inversion Principle (DIP)...")

	fmt.Println("\n```\n" + `type CreditCardPayment interface {
  Process()
}

type PayPalPayment interface {
  Process()
}

type PaymentMethod interface {
  Process()
}

type GoodPaymentProcessor interface {
  Process()
}

type creditCardPayment struct{}

func NewCreditCardPayment() CreditCardPayment {
  var creditCardPayment creditCardPayment = creditCardPayment{}
  return &creditCardPayment
}

func (creditCardPayment *creditCardPayment) Process() {
  fmt.Println("Credit card payment processed!")
}

type payPalPayment struct{}

func NewPayPalPayment() PayPalPayment {
  var payPalPayment payPalPayment = payPalPayment{}
  return &payPalPayment
}

func (payPalPayment *payPalPayment) Process() {
  fmt.Println("PayPal payment processed!")
}

type goodPaymentProcessor struct {
  method PaymentMethod
  _      struct{}
}

func NewGoodPaymentProcessor(method PaymentMethod) GoodPaymentProcessor {
  var paymentProcessor goodPaymentProcessor = goodPaymentProcessor{
    method: method,
  }

  return &paymentProcessor
}

func (paymentProcessor *goodPaymentProcessor) Process() {
  paymentProcessor.method.Process()
}` + "\n```")

	fmt.Println(
		"\nThis is a good implementation of Dependency Inversion Principle (DIP),\n" +
			"because 'goodPaymentProcessor' class depends solely on injected dependencies\n" +
			"that implement the 'PaymentMethod' interface. So, if the 'method' attribute in\n" +
			"the 'goodPaymentProcessor' class needs to be changed, the constructor does not\n" +
			"require modification (only the class call needs to be updated). For example, I\n" +
			"could inject inside the 'method' attribute an instance of 'creditCardPayment'\n" +
			"or 'payPalPayment' classes.",
	)

	fmt.Println(
		"\n# ---------------------------------------------------------------------------------- #",
	)

	/*
	   Additional challenge...
	*/

	fmt.Println("\nAdditional challenge...")

	var emailService NotificationService = NewEmailService()
	var pushService NotificationService = NewPushService()
	var smsService NotificationService = NewSMSService()

	var emailNotificationSystem NotificationSystem = NewNotificationSystem(emailService)
	var pushNotificationSystem NotificationSystem = NewNotificationSystem(pushService)
	var smsNotificationSystem NotificationSystem = NewNotificationSystem(smsService)

	fmt.Println()
	emailNotificationSystem.SendNotification()

	fmt.Println()
	pushNotificationSystem.SendNotification()

	fmt.Println()
	smsNotificationSystem.SendNotification()
}
