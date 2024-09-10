package com.acme.modres.messaging;

import javax.annotation.Resource;
import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import javax.jms.JMSConnectionFactory;
import javax.jms.JMSConsumer;
import javax.jms.JMSContext;
import javax.jms.JMSException;
import javax.jms.Queue;
import javax.jms.TextMessage;

@ApplicationScoped
public class ChatReceiver {

  @Inject
  @JMSConnectionFactory("jms/mmxCf")
  JMSContext context;

  @Resource(lookup = "jms/mmxQueue")
  Queue queue;

  public ChatReceiver() {
  }

  public String receive() throws JMSException {
    String appId = ChatProducer.APP_IDENTIFIER;
    JMSConsumer consumer = context.createConsumer(queue, "appId = '" + appId + "'");

    TextMessage message = (TextMessage) consumer.receive();
    String text = message.getBody(String.class);
    System.out.println("Message dequeued: " + text);
    return text;
  }

}