"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Plus, Minus, Trash } from "lucide-react";

// Define types
type Dish = {
  id: number;
  name: string;
  price: number;
  description: string;
};

type OrderItem = {
  dish: Dish;
  quantity: number;
};

// Sample menu data
const menuData: Dish[] = [
  { id: 1, name: "Margherita Pizza", price: 12.99, description: "Classic tomato and mozzarella" },
  { id: 2, name: "Caesar Salad", price: 8.99, description: "Romaine lettuce with Caesar dressing" },
  { id: 3, name: "Grilled Salmon", price: 18.99, description: "Fresh salmon with herbs" },
  { id: 4, name: "Beef Burger", price: 14.99, description: "Juicy beef patty with fries" },
  { id: 5, name: "Pasta Carbonara", price: 13.99, description: "Creamy pasta with bacon" },
  { id: 6, name: "Chocolate Cake", price: 6.99, description: "Rich chocolate dessert" },
];

export default function RestaurantApp() {
  const [order, setOrder] = useState<OrderItem[]>([]);
  const [isPaymentProcessing, setIsPaymentProcessing] = useState(false);

  // Add dish to order
  const addToOrder = (dish: Dish) => {
    setOrder(prevOrder => {
      const existingItem = prevOrder.find(item => item.dish.id === dish.id);
      
      if (existingItem) {
        return prevOrder.map(item => 
          item.dish.id === dish.id 
            ? { ...item, quantity: item.quantity + 1 } 
            : item
        );
      } else {
        return [...prevOrder, { dish, quantity: 1 }];
      }
    });
  };

  // Remove dish from order
  const removeFromOrder = (dishId: number) => {
    setOrder(prevOrder => {
      return prevOrder
        .map(item => 
          item.dish.id === dishId 
            ? { ...item, quantity: item.quantity - 1 } 
            : item
        )
        .filter(item => item.quantity > 0);
    });
  };

  // Remove entire item from order
  const removeItem = (dishId: number) => {
    setOrder(prevOrder => prevOrder.filter(item => item.dish.id !== dishId));
  };

  // Calculate total
  const total = order.reduce(
    (sum, item) => sum + item.dish.price * item.quantity,
    0
  );

  // Handle payment
  const handlePayment = () => {
    setIsPaymentProcessing(true);
    // Simulate payment processing
    setTimeout(() => {
      alert(`Payment of $${total.toFixed(2)} processed successfully!`);
      setOrder([]);
      setIsPaymentProcessing(false);
    }, 1500);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-amber-50 to-orange-50 p-4 md:p-8">
      <div className="max-w-6xl mx-auto">
        <header className="text-center mb-10">
          <h1 className="text-4xl md:text-5xl font-bold text-amber-900 mb-2">Delicious Bistro</h1>
          <p className="text-amber-700">Authentic cuisine made with fresh ingredients</p>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Menu Section */}
          <div className="lg:col-span-2">
            <Card className="shadow-lg">
              <CardHeader>
                <CardTitle className="text-2xl text-amber-800">Our Menu</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {menuData.map((dish) => (
                    <Card key={dish.id} className="flex flex-col">
                      <div className="p-4 flex-grow">
                        <div className="flex justify-between items-start">
                          <h3 className="font-bold text-lg text-amber-900">{dish.name}</h3>
                          <span className="font-bold text-amber-700">${dish.price.toFixed(2)}</span>
                        </div>
                        <p className="text-gray-600 text-sm mt-1">{dish.description}</p>
                      </div>
                      <div className="p-4 pt-0">
                        <Button 
                          onClick={() => addToOrder(dish)}
                          className="w-full bg-amber-600 hover:bg-amber-700"
                        >
                          Add to Order
                        </Button>
                      </div>
                    </Card>
                  ))}
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Order Summary */}
          <div>
            <Card className="shadow-lg h-full">
              <CardHeader>
                <CardTitle className="text-2xl text-amber-800">Your Order</CardTitle>
              </CardHeader>
              <CardContent>
                {order.length === 0 ? (
                  <div className="text-center py-8 text-gray-500">
                    <p>Your order is empty</p>
                    <p className="mt-2">Add items from the menu</p>
                  </div>
                ) : (
                  <>
                    <div className="space-y-4 max-h-96 overflow-y-auto pr-2">
                      {order.map((item) => (
                        <div 
                          key={item.dish.id} 
                          className="flex items-center justify-between p-3 border-b border-amber-100"
                        >
                          <div className="flex-1">
                            <h4 className="font-medium text-amber-900">{item.dish.name}</h4>
                            <p className="text-sm text-gray-600">${item.dish.price.toFixed(2)} each</p>
                          </div>
                          
                          <div className="flex items-center space-x-2">
                            <Button 
                              size="sm" 
                              variant="outline" 
                              onClick={() => removeFromOrder(item.dish.id)}
                              className="h-8 w-8 p-0"
                            >
                              <Minus className="h-4 w-4" />
                            </Button>
                            
                            <span className="w-8 text-center font-medium">{item.quantity}</span>
                            
                            <Button 
                              size="sm" 
                              variant="outline" 
                              onClick={() => addToOrder(item.dish)}
                              className="h-8 w-8 p-0"
                            >
                              <Plus className="h-4 w-4" />
                            </Button>
                            
                            <Button 
                              size="sm" 
                              variant="ghost" 
                              onClick={() => removeItem(item.dish.id)}
                              className="h-8 w-8 p-0 text-red-500 hover:text-red-700 hover:bg-red-50"
                            >
                              <Trash className="h-4 w-4" />
                            </Button>
                          </div>
                        </div>
                      ))}
                    </div>
                    
                    <div className="mt-6 pt-4 border-t border-amber-200">
                      <div className="flex justify-between text-lg font-bold mb-4">
                        <span>Total:</span>
                        <span>${total.toFixed(2)}</span>
                      </div>
                      
                      <Button 
                        onClick={handlePayment}
                        disabled={isPaymentProcessing || total === 0}
                        className="w-full bg-green-600 hover:bg-green-700 text-white py-6 text-lg"
                      >
                        {isPaymentProcessing ? "Processing..." : `Pay $${total.toFixed(2)}`}
                      </Button>
                    </div>
                  </>
                )}
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
}